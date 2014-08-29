x=[1;2;3;4;5];
y=[9.1191; 18.1189; 30.9962; 48.0327; 69.0175];

n=length(x);
A = [ones(n,1),x,x.*x]; % design matrix
a = pinv(A)*y           % pseudo inverse built in

fprintf('Lsq result via pseudo inverse\n');
fprintf('a0=%f a1=%f a2=%f\n\n',a[1],a[2],a[3]);
 

xpower2 = x.*x;
xpower3 = xpower2.*x;
xpower4 = xpower3.*x;

Y = sum(y)/n;
YX = sum(y.*x)/n;
YXX = sum(y.*xpower2)/n;
X1 = sum(x)/n;
X2 = sum(xpower2)/n;
X3 = sum(xpower3)/n;
X4 = sum(xpower4)/n;

B = [1,X1,X2;X1,X2,X3;X2,X3,X4];
a = inv(B)*[Y;YX;YXX]


sigma = 0.04;
sigmap = 0.04;
ratsq = (sigma/sigmap)^2;

C=[ratsq/n+1,X1,X2;X1,X2,X3;X2,X3,X4];
a= inv(C)*[Y+4*ratsq/n;YX;YXX]

sigma = 0.04;
sigmap = 0.001;
ratsq = (sigma/sigmap)^2;

C=[ratsq/n+1,X1,X2;X1,X2,X3;X2,X3,X4];
a= inv(C)*[Y+4*ratsq/n;YX;YXX]
