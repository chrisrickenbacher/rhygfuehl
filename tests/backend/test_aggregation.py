from aggregation import calculate_quality

def test_calculate_quality_excellent():
    # Perfect conditions: No rain, high radiation, warm water
    assert calculate_quality(
        rain_week=[0, 0, 0],
        global_radiation_week=[200, 200, 200],
        water_temp_latest=20.0,
        water_temp_48h_avg=20.0
    ) == 3

def test_calculate_quality_cold_shock():
    # Good weather but cold water below 14.0
    assert calculate_quality(
        rain_week=[0, 0, 0],
        global_radiation_week=[200, 200, 200],
        water_temp_latest=13.5,
        water_temp_48h_avg=13.5
    ) == 1

def test_calculate_quality_extreme_heat():
    # Good weather but sustained water heat above 22.0 (bacterial risk)
    # Even if latest is 21, if avg is 23, it should cap at level 2
    assert calculate_quality(
        rain_week=[0, 0, 0],
        global_radiation_week=[200, 200, 200],
        water_temp_latest=21.0,
        water_temp_48h_avg=23.0
    ) == 2

def test_calculate_quality_heavy_rain():
    # Lots of rain recently
    assert calculate_quality(
        rain_week=[10, 5, 2],
        global_radiation_week=[50, 50, 50],
        water_temp_latest=20.0,
        water_temp_48h_avg=20.0
    ) == 1

def test_calculate_quality_uv_bonus():
    # Moderate rain but high UV bonus (uv_bonus > 1.2)
    # rain_impact = (0.4 * 1.0) + (0 * 0.5) + (0 * 0.25) = 0.4 (< 0.5)
    # Actually let's test the second condition: rain_impact < 2.0 and uv_bonus > 1.2
    assert calculate_quality(
        rain_week=[0.6, 0.1, 0.1],
        global_radiation_week=[250, 250, 250],
        water_temp_latest=20.0,
        water_temp_48h_avg=20.0
    ) == 3
