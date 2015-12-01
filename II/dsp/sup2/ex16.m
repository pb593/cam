[y, Fs] = audioread('touchtone.wav');
specgram(y, [], Fs);
xlim([0 4.5]);
ylim([0 2e+3]);

% sequence is: 900441223334676