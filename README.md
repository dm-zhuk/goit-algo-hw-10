## Summary of Monte Carlo Integration of \( f(x) = x^2 \)

This code demonstrates the use of the Monte Carlo method to estimate the definite integral.

### Key Components:

1. **Function Definition**: The function to be integrated is defined as \( f(x) = x^2 \).
2. **Analytical Integration**: The integral is calculated using SciPy's `quad` function for an exact result.
3. **Monte Carlo Simulation**:
   - A specified number of random points are generated within the integration limits.
   - The proportion of points that fall under the curve is used to estimate the area under the curve, providing an approximation of the integral.
4. **Visualization**:
   - The function, area under the curve, and random points are visualized in a plot.
   - The graph includes vertical lines indicating the limits of integration, enhancing clarity.

### Results:

- The analytical integral result is printed along with the Monte Carlo estimate, allowing for comparison and validation of the Monte Carlo method's accuracy.
- Visual representation aids in understanding how the Monte Carlo method approximates the area under the curve.

### Conclusion:

This implementation effectively illustrates the Monte Carlo integration technique, showcasing its utility and providing insights into its accuracy compared to analytical methods.

### Backup data:

Аналітичний інтеграл: 2.666666666666667
Інтеграл за методом Монте-Карло: 2.5944

![Example Image](/img/Figure_1.png)
