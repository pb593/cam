% (a)
% N1 * 40k / 256 = 852 => N1 = 5 and 6
% N2 * 40k / 256 = 1477 => N2 = 9 and 10

% (b)
[y, Fs] = audioread('touchtone.wav');
specgram(y, [], Fs);
xlim([0 4.5]);
ylim([0 2e+3]);

% sequence is: 900441223334676