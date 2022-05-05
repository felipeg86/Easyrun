R5 = 3.5714;
R3v3 = 5.3475204998;
L=100e-6;
C=4.7e-6;
R_L=56e-3;
R_se=1e-3;
Vf=10.94;
tf5=calcularTF(R5, L, C, R_L, R_se, Vf);
tf3v3=calcularTF(R3v3, L, C, R_L, R_se, Vf);

function transferencia = calcularTF(R, L, C, R_L, R_se, Vf)
    H1 = tf([(C*R+R_se*C)*Vf, Vf],...
            [L*C*(R+R_se), R_L*C*R+R_L*C*R_se+R*C*R_se+L, R_L+R]);
    H2 = tf([R*C*R_se, R],...
            [C*(R+R_se), 1]); 
    transferencia = H1*H2;
end