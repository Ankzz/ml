Here’s a structured **quiz on eigenvalues and eigenvectors** to test both conceptual and applied understanding.  

---

### 📘 Quiz: Eigenvalues & Eigenvectors  

**Q1.** For a square matrix \(A\), an eigenvector \(v\) satisfies:  
- A. \(Av = v\)  
- B. \(Av = \lambda v\)  
- C. \(Av = v^2\)  
- D. \(Av = \lambda A\)  
**Answer:** B  
**Explanation:** By definition, eigenvectors satisfy \(Av = \lambda v\), where \(\lambda\) is the eigenvalue.  

---

**Q2.** The eigenvalues of a triangular matrix (upper or lower) are:  
- A. Always zero  
- B. The diagonal entries  
- C. The sum of diagonal entries  
- D. The product of diagonal entries  
**Answer:** B  
**Explanation:** For triangular matrices, eigenvalues are exactly the diagonal elements.  

---

**Q3.** If a matrix has an eigenvalue \(\lambda = 0\), what does this imply?  
- A. The matrix is invertible  
- B. The matrix is singular  
- C. The matrix is diagonalizable  
- D. The matrix has full rank  
**Answer:** B  
**Explanation:** A zero eigenvalue means the determinant is zero, so the matrix is singular (non-invertible).  

---

**Q4.** The geometric multiplicity of an eigenvalue is:  
- A. The number of times it appears in the characteristic polynomial  
- B. The dimension of its eigenspace  
- C. Always equal to its algebraic multiplicity  
- D. The determinant of the matrix  
**Answer:** B  
**Explanation:** Geometric multiplicity is the dimension of the eigenspace (number of independent eigenvectors).  

---

**Q5.** In PCA, eigenvectors of the covariance matrix represent:  
- A. Directions of maximum variance  
- B. Scaling factors of the data  
- C. The mean of the dataset  
- D. The determinant of the dataset  
**Answer:** A  
**Explanation:** Eigenvectors of the covariance matrix are the principal components, i.e., directions of maximum variance.  

---

Here’s a **challenge-level quiz on eigenvalues and eigenvectors**, designed to stretch your understanding beyond the basics.  

---

### 🔥 Advanced Quiz: Eigenvalues & Eigenvectors  

**Q1.** If a matrix \(A\) has an eigenvalue \(\lambda = 0\), which of the following is necessarily true?  
- A. \(A\) is invertible  
- B. \(\det(A) = 0\)  
- C. \(A\) must be diagonalizable  
- D. All eigenvectors are zero  
**Answer:** B  
**Explanation:** A zero eigenvalue implies the determinant is zero, so the matrix is singular (non-invertible).  

---

**Q2.** Consider a 3×3 matrix with eigenvalues \(\{2, 2, 3\}\). Which statement is correct?  
- A. The algebraic multiplicity of eigenvalue 2 is 1  
- B. The geometric multiplicity of eigenvalue 2 must equal 2  
- C. The matrix may or may not be diagonalizable depending on the eigenspace dimension of eigenvalue 2  
- D. The determinant of the matrix is 7  
**Answer:** C  
**Explanation:** Algebraic multiplicity of 2 is 2, but geometric multiplicity could be 1 or 2. If GM = AM, the matrix is diagonalizable; otherwise, it is defective.  

---

**Q3.** The sum of all eigenvalues of a matrix equals:  
- A. The determinant of the matrix  
- B. The trace of the matrix  
- C. The rank of the matrix  
- D. The number of independent eigenvectors  
**Answer:** B  
**Explanation:** The sum of eigenvalues (counted with multiplicity) equals the trace of the matrix.  

---

**Q4.** Which of the following is true about eigenvectors corresponding to distinct eigenvalues of a symmetric matrix?  
- A. They are always linearly dependent  
- B. They are always orthogonal  
- C. They must have the same length  
- D. They are always complex  
**Answer:** B  
**Explanation:** For symmetric (real) matrices, eigenvectors corresponding to distinct eigenvalues are orthogonal.  

---

**Q5.** In differential equations, eigenvalues of the system matrix determine:  
- A. The stability and type of solutions (growth/decay/oscillation)  
- B. The determinant of the system  
- C. The number of solutions  
- D. The trace of the system  
**Answer:** A  
**Explanation:** Eigenvalues indicate whether solutions grow, decay, or oscillate — crucial for stability analysis.  

---

Here’s a **challenge-level quiz on eigenvalues and eigenvectors**, designed to probe deeper theoretical and applied aspects.  

---

### 🔥 Advanced Challenge Quiz: Eigenvalues & Eigenvectors  

**Q1.** If a 4×4 matrix has eigenvalues \(\{0, 0, 3, 5\}\), which statement is correct?  
- A. The matrix is invertible  
- B. The determinant is 0  
- C. The trace is 15  
- D. The matrix must be diagonalizable  
**Answer:** B  
**Explanation:** The determinant is the product of eigenvalues. Since two eigenvalues are zero, the determinant = 0, making the matrix singular.  

---

**Q2.** For a defective matrix, which condition holds?  
- A. Geometric multiplicity < Algebraic multiplicity for at least one eigenvalue  
- B. All eigenvalues are distinct  
- C. The matrix cannot be triangularized  
- D. The determinant must be zero  
**Answer:** A  
**Explanation:** A defective matrix lacks enough independent eigenvectors, so GM < AM for some eigenvalue.  

---

**Q3.** The eigenvalues of a matrix \(A\) and its inverse \(A^{-1}\) are related by:  
- A. Reciprocal relationship: if \(\lambda\) is eigenvalue of \(A\), then \(1/\lambda\) is eigenvalue of \(A^{-1}\)  
- B. They are identical  
- C. They differ by a constant shift  
- D. They are negatives of each other  
**Answer:** A  
**Explanation:** If \(Av = \lambda v\), then \(A^{-1}v = \frac{1}{\lambda}v\).  

---

**Q4.** For a symmetric matrix, which property of eigenvectors is guaranteed?  
- A. They are always complex  
- B. They are orthogonal for distinct eigenvalues  
- C. They must all have unit length  
- D. They are linearly dependent  
**Answer:** B  
**Explanation:** Symmetric matrices have real eigenvalues, and eigenvectors corresponding to distinct eigenvalues are orthogonal.  

---

**Q5.** In the Jordan canonical form, the presence of Jordan blocks larger than 1×1 indicates:  
- A. The matrix is diagonalizable  
- B. The matrix is defective  
- C. The matrix has distinct eigenvalues  
- D. The determinant is nonzero  
**Answer:** B  
**Explanation:** Jordan blocks larger than 1×1 occur when geometric multiplicity < algebraic multiplicity, meaning the matrix is defective.  

---