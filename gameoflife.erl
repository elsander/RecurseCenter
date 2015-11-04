% sime four-square game of life written in Erlang, to get
% basic familiarity with the language!

-module(gameoflife).
-export([ping/2, start/0, clock/1]).

clock(0) ->
    Cells = [ul, ur, ll, lr],
    lists:map(fun(Cell) -> timer:send_after(1000, Cell, kill) end, Cells),
    exit(normal);
clock(Steps) ->
    Cells = [ul, ur, ll, lr],
    lists:map(fun(Cell) -> timer:send_after(1000, Cell, update) end, Cells),
    clock_receive(length(Cells)),
    clock(Steps-1).

clock_receive(0) ->
    ok;
clock_receive(N) ->
    receive
        {update, Cell, State} ->
            io:format("received ~p ~p~n", [Cell, State])
%            put(Cell, State)
    end,
    clock_receive(N - 1).

gol(State, Acc) ->
    % How many live neighbors?
    N = lists:sum(Acc),
    if 
        State == 1 ->
            if 
                N < 2; N > 3 ->
                    NewState = 0;
                true ->
                    NewState = State
            end;		      
	State == 0 ->	    
            if 
                N == 3 ->
                    NewState = 1;
                true ->
                    NewState = State
            end		      
    end,		      
    NewState.

% implement message passing between cells to get state
% scopes in erlang?
ping(A, Cells) ->
    io:format("ping intialize cell ~p~n", [A]),
    if 
        A =:= ul; A =:= lr ->
             ping(A, 0, Cells, []);
        true ->
             ping(A, 1, Cells, [])
    end.
	

ping(A, State, Cells, Acc) ->
    %check if we've received all messages we need
    %io:format("Cell ~p Acc ~p~n", [A, Acc]),
    if 
        length(Acc) == (length(Cells) - 1) ->
            New_State = gol(State, Acc),
            clock_master ! {update, A, New_State};
        true ->
	    % This will allow us to pass New_State instead of State
            % to ping later on
            New_State = State,
            ok
    end,
    receive
        update ->
            {_, _, C} = time(),
            io:format("Update time ~p~n", [C]),
            Other_Cells = lists:filter(fun(X) -> X =/= A end, Cells),
            % pass messages to other cells
            F = fun(Cell) -> Cell ! {get_state, A} end,
	    lists:map(F, Other_Cells),
            ping(A, New_State, Cells, []);
        {get_state, Cell} -> 
	    % give state to other cells
            Cell ! {send_state, State},
            ping(A, New_State, Cells, Acc);
        {send_state, CellState} ->
            % get state from other cells
            ping(A, New_State, Cells, [CellState|Acc]);
         kill ->
             exit(normal)
    end.

% convert atoms to variables that represent cartesian grid
start() ->
    Cells = [ul, ur, ll, lr],
    F = fun(X) -> register(X, spawn(gameoflife, ping, [X, Cells])) end,
    lists:map(F, Cells),
    register(clock_master, spawn(gameoflife, clock, [10])).

% can you send messages to top level (unspawned process)?
