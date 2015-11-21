% generate 1-sec Gaussian noise at 300 HZ (300 random numbers basically)
r = randn(1, 300);

% generate the filter coefficients
lo_pass45 = fir1(50, 45/150);

% now filter the signal
x = filtfilt(lo_pass45, 1, r); % do the filtering

% resample x to lower freq = 100Hz
y = zeros(1, length(x));
for i = 1:length(x)
    if mod(i, 3) == 0 
        y(i) = x(i);
    end
end

% generate low pass filter with cut-off freq 50Hz
lo_pass50 = fir1(50, 55/150);
z = 3 * filtfilt(lo_pass50, 1, y); %apply filter

plot(x, '--r'); hold on
plot(y, 'og'); hold on
plot(z, '--b'); hold on
legend('Xn (45Hz Signal)', 'Yn (100Hz sample)', 'Zn (reconstructed)');