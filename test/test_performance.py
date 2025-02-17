from src.NetworkInfo import get_network_data
from src.metricsInfo import get_performance_metrics
import pandas as pd
import pytest
import time

# PyTest case
@pytest.mark.parametrize("iteration", range(3))  # Run test multiple times
def test_network_performance(iteration):
    network_data = get_network_data()
    perf_data = get_performance_metrics()

    # Merge results
    data = {**network_data, **perf_data, "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

    # Save to CSV
    df = pd.DataFrame([data])
    df.to_csv("network_performance_logs.csv", mode='a', index=False, header=False)

    print("✅ Test Iteration:", iteration + 1, "Data:", data)