# Neural Operator in Tangent Space for the Exponential Representation of Kinematics in Manipulator Robots

In the realm of kinematics and motion modeling, certain mathematic tools are used to model rigid bodies.
To beging with, the Homogeneous Transformation Matrix (HTM), as shown in the equation below, is a $4\times4$ matrix composed by a rotational matrix $R$ and a translational vector $T$.

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

The reason of this fact is due to the fact that these pathematic tools always are operated with between them to represent transformations between frames of references, as in the case of robotic kinematics. This is achived with the property of multiplication of matrices and quaternions, whilst the Euler Angles don't have an operation that represent this transformations. This is the reason why 3 elements for representing orientation is not enough, and these angles must be converted in other operable elements such as rotation matrices or quaternions. Nevertheless, there is an expresion that depicts rotations and just uses 3 elements, this is the axis-angle representation:

$$
\begin{equation}
A = \vec{\mu}\theta
\end{equation}
$$

Where $\vec{\mu}$ is a unit vector, and \theta is the angle of rotation around the unit axis. However, this representation also lacks in operations to transform reference frames. For this reason, this representation is useless and must be transformed into HTM o DQ in order to operate.

On the other hand, the theory of Lie Algebra, and Riemann's Manifolds creates a relationship between the axis-angle representation with the HTM and DQ. It turns out that both HTM and DQ are the exponential map of the axis-angle notation as is shown in the following equation:

$$
\begin{equation}
e^{\vec{\mu}\theta}=cos(\theta)+\vec{\mu}sin(\theta)=Q
\end{equation}
$$

$$
\begin{equation}
e^{[\vec{\mu}\theta]}=\begin{bmatrix}
R_{1,1} & R_{1,2} & R_{1,3} \\
R_{2,1} & R_{2,2} & R_{2,3} \\
R_{3,1} & R_{3,2} & R_{3,3} \\
\end{bmatrix}
\end{equation}
$$

Where the skew matrix of a vector is:

$$
\begin{equation}
[\vec{\mu}\theta]=\begin{bmatrix}
0 & -z & y \\
z & 0 & x \\
-y & -x & 0 \\
\end{bmatrix}
\end{equation}
$$

## Bibliography
- Arimoto, S., Yoshida, M., Sekimoto, M., & Tahara, K. (2009). A Riemannian-Geometry Approach for Modeling and Control of Dynamics of Object Manipulation under Constraints. Journal of Robotics, 2009, 1–16. https://doi.org/10.1155/2009/892801
- Calinon, S. (2020). Gaussians on riemannian manifolds: Applications for robot learning and adaptive control. IEEE Robotics and Automation Magazine, 27(2), 33–45. https://doi.org/10.1109/MRA.2020.2980548
- Condurache, D., & Ciureanu, I. A. (2020). Baker-Campbell-Hausdorff-Dynkin formula for the lie algebra of rigid body displacements. Mathematics, 8(7), 1–19. https://doi.org/10.3390/math8071185
- da Silva, I. N., Spatti, D. H., Flauzino, R. A., Liboni, L. H. B., & dos Reis Alves, S. F. (2016). Artificial neural networks: A practical course. In Artificial Neural Networks: A Practical Course (Vol. 50, Issue 2). Springer International Publishing. https://doi.org/10.1007/978-3-319-43162-8
- DİKMENLİ, S. (2022). Forward & Inverse Kinematics Solution of 6-Dof Robots Those Have Offset & Spherical Wrists. Eurasian Journal of Science Engineering and Technology, 3(1), 14–28. https://doi.org/10.55696/ejset.1082648
- Khan, G. M. (2018). Artificial neural network (ANNs). Studies in Computational Intelligence, 725(Sordo), 39–55. https://doi.org/10.1007/978-3-319-67466-7_4
- Kumar, S. (2008). INTRODUCCION A LA ROBOTICA (Vol. 1).
- Larotonda, G., & Varela, A. (2018). CURVAS Y SUPERFICIES. 105.
- Li, Y., Zhao, Y., Zhang, T., & Li, T. (2019). Forward kinematics analysis and experiment of hybrid high-altitude board installation robot based on screw theory. Advances in Mechanical Engineering, 11(4), 1–11. https://doi.org/10.1177/1687814019846266
- Pampano, A. (2014). Geodesicas en Variedades de Riemann.
- Pham, D. T., Packianather, M. S., & Afify, A. A. (2008). Artificial neural networks. Computational Intelligence: For Engineering and Manufacturing, 67–92. https://doi.org/10.1007/0-387-37452-3_3
- Radavelli, L. A., Simoni, R., Pieri, E. De, & Martins, D. (2012). A Comparative Study of the Kinematics of Robots Manipulators by Denavit-Hartenberg and Dual Quaternion. Mecánica Computacional, Multi-Body …, XXXI(September 2014), 13–16. http:%0Awww.joinville.ufsc.br/%0Awww.mtm.ufsc.br%0Ahttp://scholar.google.com/scholar?hl=en&btnG=Search&q=intitle:A+COMPARATIVE+STUDY+OF+THE+KINEMATICS+OF+ROBOTS+MANIPULATORS+BY+DENAVIT-HARTENBERG+AND+DUAL+quaternion#2
- Siciliano, B., Sciavicco, L., Villani, L., & Oriolo, G. (2009). Robotics. Springer London. https://doi.org/10.1007/978-1-84628-642-1
