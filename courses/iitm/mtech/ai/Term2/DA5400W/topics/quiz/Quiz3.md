Alright, let’s **push the quiz into a deeper challenge mode** with numerical problems that require explicit computation or reasoning. These will feel more exam-style and hands-on.  

---

### 🔥 Challenge+ Quiz: PCA, Determinants, Eigenvalues, Jordan Form, Optimization  

**Q1. (Determinant)**  
Compute the determinant of  
$
A = \begin{bmatrix} 3 & 2 & 1 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{bmatrix}
$  
- A. 72  
- B. 60  
- C. 36  
- D. 24  

---

**Q2. (Eigenvalues & Eigenvectors)**  
Find the eigenvalues of  
$
B = \begin{bmatrix} 4 & 2 \\ 2 & 4 \end{bmatrix}
$  
and identify the eigenvector corresponding to the smaller eigenvalue.  
- A. Eigenvalues: 2, 6; Eigenvector for 2 is $[1, -1]^T$  
- B. Eigenvalues: 4, 4; Eigenvector for 4 is $[1, 0]^T$  
- C. Eigenvalues: 0, 8; Eigenvector for 0 is $[1, -1]^T$  
- D. Eigenvalues: 2, 6; Eigenvector for 2 is $[1, 1]^T$  

---

**Q3. (PCA)**  
A covariance matrix has eigenvalues $[10, 5, 5]$. How many principal components are needed to explain at least 80% of the variance?  
- A. 1  
- B. 2  
- C. 3  
- D. Cannot be determined  

---

**Q4. (Jordan Form)**  
Matrix  
$
C = \begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix}
$  
has eigenvalue $\lambda = 3$. Which statement is correct?  
- A. Jordan form is diagonal with entries (3,3)  
- B. Jordan form has a single Jordan block of size 2  
- C. Jordan form has eigenvalues 2 and 4  
- D. Jordan form is the identity matrix  

---

**Q5. (Quadratic Optimization)**  
Minimize  
$
f(x) = x^T Q x + c^T x
$  
with  
$
Q = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}, \quad c = \begin{bmatrix} -4 \\ -6 \end{bmatrix}.
$  
Where does the minimum occur?  
- A. $(1,1)$  
- B. $(2,3)$  
- C. $(0,0)$  
- D. $(4,6)$  

---

**Q6. (Multiplicity & Diagonalizability)**  
A 3×3 matrix has eigenvalues $\{2, 2, 2\}$ but only one independent eigenvector. Which statement is true?  
- A. The matrix is diagonalizable  
- B. The matrix is defective and has a Jordan block of size 3  
- C. The matrix is orthogonal  
- D. The matrix is positive definite  

---

### ✅ Consolidated Answers
1. A (det = product of diagonal entries = $3 \cdot 4 \cdot 6 = 72$)  
2. A (characteristic polynomial → eigenvalues 2, 6; eigenvector for 2 is $[1, -1]^T$)  
3. B (total variance = 20; first two eigenvalues = 15 → 15/20 = 75%; need 2 components to reach ≥80%) → correction: actually need **all 3** since 15/20 = 75% < 80%. Answer = **C**  
4. B (defective matrix → Jordan block of size 2)  
5. B (gradient = $2x + c = 0$ → solution $(2,3)$)  
6. B (algebraic multiplicity 3, geometric multiplicity 1 → defective, Jordan block size 3)  

---