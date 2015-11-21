b = [1, 0, 0, 2, 2];

% First, make up the matrix A and multiply it by vector b
a = [-3, 2, 1];
r = [a(3), 0, 0, 0, 0];
c = [fliplr(a), 0, 0, 0, 0];
A = toeplitz(c, r)

rst1 = transpose(mtimes(A, transpose(b)))
% Now, let's do it using the conv func
rst2 = conv(fliplr(a), b)

% Now let's try to undo the convolution
origb = int8(transpose(A \ transpose(rst2)))
origa = fliplr(deconv(rst2, b))







