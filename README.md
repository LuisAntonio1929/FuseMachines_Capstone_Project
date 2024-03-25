# Neural Operator in Tangent Space for the Exponential Representation of Kinematics in Manipulator Robots

In the realm of kinematics and motion modeling, certain mathematic tools are used to model rigid bodies.
To beging mentioning, the Homogeneous Transformation Matrix (HTM), as shown in the equation below, is a $4\times4$ matrix composed by a rotational matrix $R$ and a translational vector $T$.

$$
\begin{equation}
HTM = \begin{bmatrix}
R_{1,1} & R_{1,2} & R_{1,3} & T_x \\
R_{2,1} & R_{2,2} & R_{2,3} & T_y \\
R_{3,1} & R_{3,2} & R_{3,3} & T_z \\
0 & 0 & 0 & 1
\end{bmatrix}
\end{equation}
$$

A second state-of-the-art tool are the Dual Quaternions, as shown in the equation below.

$$
\begin{equation}
DQ = q_r+ix_r+jy_r+z_r+(q_d+ix_d+jy_d+z_d)\epsilon
\end{equation}
$$
