% define observation sequence
z{2} = [1.2 ; -0.1];
z{3} = [1.1 ; -0.4];
z{4} = [-0.5 ; 0.5];
z{5} = [1.2 ; -0.8];

% Set the prior mean mu_{1|1} using a cell array
mu{1,1} = [1; 0];

% Set the prior covariance Sigma_{1|1} using a cell array
Sigma{1,1} = eye(2);

% define dynamics noise covariance
sigma = 0.05;
Q = sigma^2 * eye(2);

% define observation noise covariance
rho = 0.4;
R = rho^2 * eye(2);

for t = 2:5;
    % prediction
    
    mu{t,t-1} = [ sin( mu{t-1,t-1}(1) ); 
                  mu{t-1,t-1}(2) ];
    
    grad_f = [ cos( mu{t-1,t-1}(1) ), 0; 
               0, mu{t-1,t-1}(2)];
    
    Sigma{t,t-1} = grad_f * Sigma{t-1,t-1} * grad_f' + Q;

    % Fuse measurement with prediction
    
    Sigma{t,t} = inv( inv(Sigma{t,t-1}) + inv(R) );
    
    mu{t,t} = ...
        Sigma{t,t} * ( inv(Sigma{t,t}) * mu{t,t-1} + inv(R) * z{t} );
end

% compute the expected loss for Q3h
sdx =  sqrt(Sigma{5,5}(1,1));
sdy =  sqrt(Sigma{5,5}(2,2));

exp_loss = 0.1 * 10 ...
    - 3 * 0.9 * (normcdf(0.1, 0, sdx) - normcdf(-0.1, 0, sdx)) * ...
                (normcdf(0.1, 0, sdy) - normcdf(-0.1, 0, sdy));