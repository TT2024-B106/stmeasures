#include "amss.h"
// #include <stdio.h>

#define PI 3.141592653589793
#define MAX(a, b) ((a) > (b) ? (a) : (b))

double dot_product(const double *a, const double *b) {
    return a[0] * b[0] + a[1] * b[1];
}

double magnitude(const double *a) {
    return sqrt(a[0] * a[0] + a[1] * a[1]);
}

double similarity(const double *r, const double *s) {
    double mag_r = magnitude(r);
    double mag_s = magnitude(s);

    if (mag_r == 0.0 || mag_s == 0.0) {
        return 0.0; // Avoid division by zero
    }

    double dot = dot_product(r, s);
    double cos_theta = dot / (mag_r * mag_s);

    // Clamp cos_theta to avoid floating-point precision issues
    if (cos_theta < -1.0) cos_theta = -1.0;
    if (cos_theta > 1.0) cos_theta = 1.0;

    double theta = acos(cos_theta);

    if (theta > PI / 2) {
        return 0.0;
    }
    return cos_theta;
}

double amss_distance(const double *r, const double *s, int n, int m) {
    double **dp = (double **) malloc((n + 1) * sizeof(double *));
    for (int i = 0; i <= n; i++) {
        dp[i] = (double *) malloc((m + 1) * sizeof(double));
    }

    // Initialize the dp array
    for (int i = 0; i <= n; i++) dp[i][0] = 0.0;
    for (int j = 0; j <= m; j++) dp[0][j] = 0.0;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            double qn[2] = {r[(i - 1) * 2], r[(i - 1) * 2 + 1]};
            double qn_1[2] = {0, 0};
            if (i >= 2) {
                qn_1[0] = r[(i - 2) * 2];
                qn_1[1] = r[(i - 2) * 2 + 1];
            }

            double cm[2] = {s[(j - 1) * 2], s[(j - 1) * 2 + 1]};
            double cm_1[2] = {0, 0};
            if (j >= 2) {
                cm_1[0] = s[(j - 2) * 2];
                cm_1[1] = s[(j - 2) * 2 + 1];
            }

            double sim_qn_cm = similarity(qn, cm);
            double sim_qn_1_cm = (i >= 2) ? similarity(qn_1, cm) : 0.0;
            double sim_qn_cm_1 = (j >= 2) ? similarity(qn, cm_1) : 0.0;

            double term1 = dp[i - 1][j - 1] + 2 * sim_qn_cm;
            double term2 = (i >= 2
                ? dp[i - 2][j - 1] + 2 * sim_qn_1_cm + sim_qn_cm : -INFINITY);
            double term3 = (j >= 2
                ? dp[i - 1][j - 2] + 2 * sim_qn_cm_1 + sim_qn_cm : -INFINITY);

            dp[i][j] = MAX(term1, MAX(term2, term3));

            // Debugging prints
            // printf("dp[%d][%d] = %f (term1=%f, term2=%f, term3=%f)\n",
            //        i, j, dp[i][j], term1, term2, term3);
        }
    }

    double result = dp[n][m];
    for (int i = 0; i <= n; i++) free(dp[i]);
    free(dp);

    return result;
}
