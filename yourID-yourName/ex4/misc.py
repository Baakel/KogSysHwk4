import matplotlib.pyplot as plt
import numpy as np


expected_output_vi_finite = """Iteration |  max|V-Vprev|  | # chg actions | V[0]    
----------+----------------+---------------+---------
   0      |   1000.00000   |      0        |    0.000
   1      |     30.00000   |     50        |    0.000
   2      |     30.00000   |     11        |    0.000
   3      |     30.00000   |      6        |    2.000
   4      |     30.00000   |      8        |    4.000
   5      |     30.00000   |      5        |    6.000
   6      |     30.00000   |      3        |    8.000
   7      |     30.00000   |      2        |   10.000
   8      |     30.00000   |      3        |   12.000
   9      |     30.00000   |      0        |   14.000
  10      |     30.00000   |      1        |   16.000
  11      |     30.00000   |      2        |   18.000
  12      |     30.00000   |      4        |   20.000
  13      |     30.00000   |      3        |   22.000
  14      |     30.00000   |      0        |   24.000"""


expected_output_vi_infinite = """Iteration |  max|V-Vprev|  | # chg actions | V[0]    
----------+----------------+---------------+---------
   0      |   1000.00000   |      0        |    0.000
   1      |     24.00000   |     50        |    0.000
   2      |     19.20000   |     11        |    0.000
   3      |     15.36000   |      6        |    1.024
   4      |     12.28800   |      8        |    1.843
   5      |      9.83040   |      5        |    2.499
   6      |      7.86432   |      3        |    3.023
   7      |      6.29146   |      2        |    3.442
   8      |      5.03316   |      0        |    3.778
   9      |      4.02653   |      2        |    4.046
  10      |      3.22123   |      0        |    4.261
  11      |      2.57698   |      0        |    4.433
  12      |      2.06158   |      3        |    4.570
  13      |      1.64927   |      1        |    4.680
  14      |      1.31941   |      2        |    4.768
  15      |      1.05553   |      3        |    4.839
  16      |      0.84442   |      1        |    4.895
  17      |      0.67554   |      1        |    4.940
  18      |      0.54043   |      1        |    4.976
  19      |      0.43235   |      0        |    5.005
  20      |      0.34588   |      0        |    5.028
  21      |      0.27670   |      0        |    5.046
  22      |      0.22136   |      0        |    5.061
  23      |      0.17709   |      1        |    5.073
  24      |      0.14167   |      0        |    5.082
  25      |      0.11334   |      0        |    5.090
  26      |      0.09067   |      0        |    5.108
  27      |      0.07254   |      0        |    5.181
  28      |      0.05803   |      0        |    5.239
  29      |      0.04642   |      0        |    5.285
  30      |      0.03714   |      0        |    5.322
  31      |      0.02971   |      0        |    5.352
  32      |      0.02377   |      0        |    5.376
  33      |      0.01901   |      0        |    5.395
  34      |      0.01521   |      0        |    5.410
  35      |      0.01217   |      0        |    5.422
  36      |      0.00974   |      0        |    5.432
  37      |      0.00779   |      0        |    5.440
  38      |      0.00623   |      0        |    5.446
  39      |      0.00498   |      0        |    5.451
  40      |      0.00399   |      0        |    5.455
  41      |      0.00319   |      0        |    5.458
  42      |      0.00255   |      0        |    5.460
  43      |      0.00204   |      0        |    5.463
  44      |      0.00163   |      0        |    5.464
  45      |      0.00131   |      0        |    5.465
  46      |      0.00105   |      0        |    5.467
  47      |      0.00084   |      0        |    5.467
  48      |      0.00067   |      0        |    5.468
  49      |      0.00054   |      0        |    5.469
  50      |      0.00043   |      0        |    5.469
  51      |      0.00034   |      0        |    5.469
  52      |      0.00027   |      0        |    5.470
  53      |      0.00022   |      0        |    5.470
  54      |      0.00018   |      0        |    5.470
  55      |      0.00014   |      0        |    5.470
  56      |      0.00011   |      0        |    5.470
  57      |      0.00009   |      0        |    5.470
  58      |      0.00007   |      0        |    5.470
  59      |      0.00006   |      0        |    5.470
  60      |      0.00005   |      0        |    5.471
  61      |      0.00004   |      0        |    5.471
  62      |      0.00003   |      0        |    5.471
  63      |      0.00002   |      0        |    5.471
  64      |      0.00002   |      0        |    5.471
  65      |      0.00002   |      0        |    5.471
  66      |      0.00001   |      0        |    5.471
  67      |      0.00001   |      0        |    5.471"""


expected_output_vi_finite_stoch = """Iteration |  max|V-Vprev|  | # chg actions | V[0]    
----------+----------------+---------------+---------
   0      |   1000.00000   |      0        |    0.000
   1      |    300.00000   |     65        |    0.000
   2      |     90.00000   |      5        |    0.000
   3      |     30.00000   |      3        |    0.100
   4      |     30.00000   |      1        |    0.310
   5      |     30.00000   |      1        |    0.641
   6      |     30.00000   |      0        |    1.088
   7      |     30.00000   |      1        |    1.650
   8      |     30.00000   |      0        |    2.318
   9      |     30.00000   |      1        |    3.088
  10      |     30.00000   |      0        |    3.953
  11      |     30.00000   |      0        |    4.905
  12      |     30.00000   |      1        |    5.939
  13      |     30.00000   |      0        |    7.050
  14      |     30.00000   |      0        |    8.230"""


expected_output_pi_infinite = """Iteration |  max|V-Vprev|  | # chg actions | V[0]    
----------+----------------+---------------+---------
   0      |   3079.69813   |      0        | -1012.685
   1      |   2079.69813   |     55        |   -0.000
   2      |    119.99789   |     24        |    5.120
   3      |     88.80000   |     15        |    5.120
   4      |     57.34400   |      8        |    5.120
   5      |     43.57120   |      5        |    5.120
   6      |     18.50440   |      5        |    5.120
   7      |      8.96281   |      8        |    5.120
   8      |      5.57025   |      4        |    5.120
   9      |      2.08000   |      3        |    5.471
  10      |      1.28000   |      1        |    5.471
  11      |      0.00000   |      0        |    5.471"""


def make_grader(expected):
    boxed_i = [0]
    boxed_err = [False]
    expected_lines = expected.split("\n")
    def checking_print(line):
        if boxed_i[0] < len(expected_lines):
            expected_line = expected_lines[boxed_i[0]]
        else:
            expected_line = "[END]"
        if expected_line == line:
            print(line)
        else:
            boxed_err[0] = True
            print("\x1b[41m", end="")
            print(line, end="")
            print("\x1b[0m", end="")
            print(" *** Expected: \x1b[42m" + expected_line + "\x1b[0m")
        boxed_i[0] += 1
        if boxed_i[0] == len(expected_lines):
            print("Test failed" if boxed_err[0] else "Test succeeded")
    return checking_print


def plot_v_pi(vf, pi, mdp):
    """
    Plots the value function of a given grid world MDP along with a policy

    @param vf: value function, 2D numpy array
    @param pi: policy, 2D numpy array
    @param mdp: mdp object
    @return: nothing
    """
    n_rows = vf.shape[0]
    n_cols = vf.shape[1]

    plt.figure(figsize=(n_rows, n_cols))
    plt.imshow(vf, cmap='gray', interpolation='none')  #, clim=(0, 1))
    ax = plt.gca()
    ax.set_xticks(np.arange(n_cols) - .5)
    ax.set_yticks(np.arange(n_rows) - .5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    Y, X = np.mgrid[0:n_rows, 0:n_cols]
    a2uv = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0), 4: (0, 0)}
    for x, y in zip(X.flatten(), Y.flatten()):
        a = pi[y, x]
        u, v = a2uv[a]
        if a != 4:
            plt.arrow(x, y, u * .3, -v * .3, color='m', head_width=0.1, head_length=0.1)
        else:
            ax.scatter(x, y, s=20,  color='m')
        plt.text(x, y, mdp.desc[y][x],
                 color='g', size=12, verticalalignment='center',
                 horizontalalignment='center', fontweight='bold')
    plt.grid(color='b', lw=2, ls='-')
    plt.show()
