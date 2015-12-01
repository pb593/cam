% read the data into MATLAB
f = fopen('iq-fm-96M-240k.dat', 'r', 'ieee-le');
c = fread(f, [2, inf], '*float');
fclose(f);

z = c(1,:) + j * c(2,:); % a bunch of complex numbers
%FM-demodulate
dt = 1 / 240e+3; % sampling period
demod = angle(z(2:end) ./ z(1:end-1)) / dt;
        %approximation from the notes

% design the low-pass Butterworth signal at 16kHz
[b, a] = butter(2, 2 * 16e+3 / 240e+3);
% apply the filter
fltrd = filter(b, a, demod);

% reduce the sample rate from 240 kHz to 48 kHz
signal = fltrd(1:5:end);
signal = signal / norm(signal) * 10;

% write output to file
audiowrite('out.wav', signal, 48e+3);