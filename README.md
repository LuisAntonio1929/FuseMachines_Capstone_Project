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

A second state-of-the-art tool are the Dual Quaternions, as shown in the equation below, which describe the position and orientation of a body using just 8 elements.

$$
\begin{equation}
DQ = q_r+ix_r+jy_r+kz_r+(q_d+ix_d+jy_d+kz_d)\epsilon
\end{equation}
$$

As can be seed, to describe a body in the space (position and attitude), the existented tools expend 16 elements in the case of HTMs, and 8 elements on the case of DQ. Nonetheless, for describing the position of an object is just requiered 3 elements (x,y,z coordinates), and for describing an orientation is also just requieres 3 elements (pitch, roll and yaw Euler angles). To sum up, it is requiered just 6 elements to describe an object in the space.   
