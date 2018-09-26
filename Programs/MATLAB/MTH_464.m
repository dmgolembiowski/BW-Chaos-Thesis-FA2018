%% r = 0.9
%
r = 0.9;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 10: end), '.', 'MarkerSize', 20)
%% r = 1.0
%
r = 1.0;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 10: end), '.', 'MarkerSize', 20)
%% r = 1.1
%
r = 1.1;
x = 1:2000;
x(1) = 0.5;
for n = 2:2000
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 10: end), '.', 'MarkerSize', 20)
%% r = 1.5
%
r = 1.5;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 10: end), '.', 'MarkerSize', 20)
%% r = 2.0
%
r = 2.0;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 10: end), '.', 'MarkerSize', 20)
%% r = 2.5
%
r = 2.5;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 10: end), '.', 'MarkerSize', 20)
%% r = 3.1
%
r = 3.5;
x = 1:2000;
x(1) = 0.5;
for n = 2:2000
    z = x(n - 1);
    x(n) = r*z*(1 - z);
    diffs(n) = abs(x(n) - x(n - 1));
end
plot(diffs(end - 10: end), '.', 'MarkerSize', 20)
axis([0 12 0 inf])
%% r = 3.25
%
r = 3.25;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 10: end), '.', 'MarkerSize', 20)
axis([0 12 0 1])
%% r = 3.5
%
r = 3.5;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 20: end), '.', 'MarkerSize', 20)
axis([0 22 0 1])
%% r = 3.55
%
r = 3.55;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 50: end), '.', 'MarkerSize', 20)
axis([0 52 0 1])
%% r = 3.57
%
r = 3.57;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 50: end), '.', 'MarkerSize', 20)
axis([0 52 0 1])
%% r = 3.7
%
r = 3.7;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 50: end), '.', 'MarkerSize', 20)
axis([0 52 0 1])
%% r = 3.84
%
r = 3.84;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 50: end), '.', 'MarkerSize', 20)
axis([0 52 0 1])
%% r = 3.845
%
r = 3.845;
x = 1:200;
x(1) = 0.5;
for n = 2:200
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 50: end), '.', 'MarkerSize', 20)
axis([0 52 0 1])
%% r = 4.0
%
r = 3.54;
x = 1:2000;
x(1) = 0.6;  % not 0.5
for n = 2:2000
    z = x(n - 1);
    x(n) = r*z*(1 - z);
end
plot(x(end - 50: end), '.', 'MarkerSize', 20)
axis([0 52 0 1 ])
%% Draw bifurcation diagram
%
close all
clear all
r_i = 3;                                 % initial value of r
r_f = 4;                                 % final value of r
steps = 500;                             % number of steps from r_i to r_f
terms = 50000;                           % number of terms x_n generated
tail = 100;                              % length of "tail" plotted
rstep = (r_f - r_i)/steps;               % space between r-values
x = 0.5*ones(steps, terms);              % pre-populate x-array with initial values
r = r_i;                                 % initialize r
for i = 1:steps                          % sweep across r-values
    for n = 1:terms                      % generate x_n's    
        z = x(i, n);                     % grab current x_n
        x(i, n + 1) = r*z*(1 - z);       % get x_(n + 1) from x_n
    end
    r = r + rstep;                       % next value of r
end
x = x(:, terms - tail : end);
rvalues = r_i:rstep:r_f - rstep;
plot(rvalues, x, 'k.', 'MarkerSize' , 3)
%% Algebra stuff for f
%
close all                                % clean slate
clear all
syms x r                                 % define symbolic variables
f = r*x*(1 - x);                         % define mapping f
solx = solve(f == x, x)                  % find fixed point of f
slope = subs(diff(f), x, solx(2))        % find f' at nonzero fixed point
simplify(slope)                          % simplify
%% Algebra stuff for f(f)
%
close all                                % clean slate
clear all
syms x r                                 % define symbolic variables
f = r*x*(1 - x);                         % define mapping f
g = compose(f, f)                        % composition g(x) = f(f(x))
solx = solve(g == x, x)                  % find fixed point of g(x)
slope = subs(diff(g), x, solx([3 4]))    % find g' where g has fixed point but f does not
simplify(slope)                          % simplify
