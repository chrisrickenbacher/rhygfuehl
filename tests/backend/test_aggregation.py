from aggregation import calculate_quality

def test_safety_index_thresholds():
    # Test Safety Index transitions (assuming perfect quality Q3)
    perfect_rain = [0, 0, 0]
    perfect_rad = [200, 200, 200]
    
    # S1: < 14.0
    assert calculate_quality(perfect_rain, perfect_rad, 13.9, 20.0)['safety'] == 1
    # S2: 14.0 <= T < 18.0
    assert calculate_quality(perfect_rain, perfect_rad, 14.0, 20.0)['safety'] == 2
    assert calculate_quality(perfect_rain, perfect_rad, 17.9, 20.0)['safety'] == 2
    # S3: >= 18.0
    assert calculate_quality(perfect_rain, perfect_rad, 18.0, 20.0)['safety'] == 3

def test_quality_index_rain_impact():
    # Test Quality Index based on rain (assuming perfect safety S3)
    safe_temp = 20.0
    perfect_rad = [200, 200, 200]
    
    # Q3: I < 0.5
    assert calculate_quality([0.4, 0, 0], perfect_rad, safe_temp, safe_temp)['quality'] == 3
    # Q2: 0.5 <= I < 3.5 AND r0 < 1.5
    assert calculate_quality([1.4, 0, 0], perfect_rad, safe_temp, safe_temp)['quality'] == 2
    # Q1: I >= 3.5
    assert calculate_quality([3.5, 0, 0], perfect_rad, safe_temp, safe_temp)['quality'] == 1
    # Q1: r0 >= 1.5 (Immediate cap)
    assert calculate_quality([1.5, 0, 0], perfect_rad, safe_temp, safe_temp)['quality'] == 1

def test_quality_rescue_logic():
    # Test Quality Index "rescue" by radiation bonus
    safe_temp = 20.0
    
    # Q3 Rescue: r0 < 1.0 AND I < 2.0 AND B > 1.2
    # B = 210/170 = 1.23
    assert calculate_quality([0.9, 0, 0], [210, 210, 210], safe_temp, safe_temp)['quality'] == 3
    # Fail Q3 Rescue: r0 = 1.0
    assert calculate_quality([1.0, 0, 0], [210, 210, 210], safe_temp, safe_temp)['quality'] == 2
    
    # Q2 Rescue: r0 < 1.5 AND I < 5.0 AND B > 1.0
    # B = 180/170 = 1.05, I = 1.4 + 2.5 + 0.5 = 4.4
    assert calculate_quality([1.4, 5.0, 2.0], [180, 180, 180], safe_temp, safe_temp)['quality'] == 2
    # Fail Q2 Rescue: B < 1.0
    assert calculate_quality([1.4, 5.0, 2.0], [150, 150, 150], safe_temp, safe_temp)['quality'] == 1

def test_quality_caps():
    # Test Quality Index Caps (Radiation Penalty & Thermal Risk)
    safe_temp = 20.0
    perfect_rain = [0, 0, 0]
    
    # Overcast Penalty: B < 0.6 (even with no rain)
    # B = 100/170 = 0.58
    assert calculate_quality(perfect_rain, [100, 100, 100], safe_temp, safe_temp)['quality'] == 1
    # Boundary: B = 0.61 (No penalty)
    assert calculate_quality(perfect_rain, [105, 105, 105], safe_temp, safe_temp)['quality'] == 3
    
    # Thermal Risk: avg > 22.0
    assert calculate_quality(perfect_rain, [200, 200, 200], safe_temp, 22.1)['quality'] == 1

def test_bottleneck_principle():
    # The overall level MUST be the minimum of Quality and Safety
    
    # Q3, S1 -> Level 1 (Cold but clean)
    res1 = calculate_quality([0, 0, 0], [200, 200, 200], 13.0, 13.0)
    assert res1['level'] == 1
    assert res1['quality'] == 3
    assert res1['safety'] == 1
    
    # Q1, S3 -> Level 1 (Warm but dirty)
    res2 = calculate_quality([5.0, 0, 0], [200, 200, 200], 20.0, 20.0)
    assert res2['level'] == 1
    assert res2['quality'] == 1
    assert res2['safety'] == 3
    
    # Q2, S2 -> Level 2
    res3 = calculate_quality([1.0, 0, 0], [200, 200, 200], 16.0, 16.0)
    assert res3['level'] == 2
