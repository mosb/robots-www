
num_trials = 10000;
% initialise the final state for each trial
s5 = nan(2, num_trials);

for trial = 1:num_trials
    % initialise x & y to nonsense values to be overwritten shortly
    x = nan(1, 5);
    y = nan(1, 5);
    
    % set first time step
    x(1) = 1;
    y(1) = 0;
    
    for i = 2:5;
        x(i) = sin(x(i-1)) + 0.05*normrnd(0,1);
        y(i) = (y(i-1)) + 0.05*normrnd(0,1);
    end;
    
    % write the final state for each trial
    s5(:, trial) = [x(5); y(5)];
    
end

mean_x = mean(s5(1, :));
mean_y = mean(s5(2, :));