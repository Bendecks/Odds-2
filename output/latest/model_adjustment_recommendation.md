# Model Adjustment Recommendation

## Flags

- High probability bands are currently negative ROI.
- Lower probability bands are currently performing better.
- Probability calibration gap is material.
- Best league so far: unknown avg_roi=-0.0095
- Worst league so far: unknown avg_roi=-0.0095
- CLV beat rate below 50%: 0.4286

## Recommended model changes

- Reduce confidence in favorites and add extra shrinkage above 0.50 probability.
- Investigate underdog/moderate-price markets before expanding favorite exposure.
- Prioritize probability calibration before adding complex model features.
- Treat all recommendations as paper-tracking until CLV improves above neutral.