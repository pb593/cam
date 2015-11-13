x = xlsread('Book.xlsx', 'Sheet1', 'A2:A13'); % read A2:A13 from Sheet1
y = xlsread('Book.xlsx', 'Sheet1', 'F2:F13');


ft = fittype( 'smoothingspline' ); 
opts = fitoptions( 'Method', 'SmoothingSpline' );
opts.Normalize = 'on';
opts.SmoothingParam = 0.5; % smoothing parameter
                           % 0 for line, 1 for perfect fit
                           % play around with this parameter

fit_result = fit(x, y, ft, opts); % do the fitting
% fit_result is an ordinary function, so can do fit_result(4.5) to see the
% value of the func at x = 4.5
figure;
plot(fit_result); % make a plot for the Little
hold;

%now calculate the errors
y_fits = ones(size(x));
for i = 1:size(x) % sample the FITTED function in the x values
    y_fits(i) = fit_result(x(i));
end

e = std(y_fits) * ones(size(x)); % standard deviation of vals in y_fits
                                 % can calculate the error in some other
                                 % way

errorbar(x, y, e, 'o'); % plot the points and the error bars
ylabel('Love for the Little');
xlabel('Time');