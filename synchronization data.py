import numpy as np
import pandas as pd

# 균등 분포 기반 합성 데이터 생성 함수
def generate_synthetic_data(num_samples, num_features, min_val, max_val):
    """
    num_samples: 생성할 샘플 수
    num_features: 속성(특징) 수
    min_val: 각 속성의 최솟값
    max_val: 각 속성의 최댓값
    """
    # 균등 분포에서 샘플링하여 데이터 생성
    data = np.random.uniform(low=min_val, high=max_val, size=(num_samples, num_features))
    
    # 데이터프레임으로 변환
    columns = [f'feature_{i+1}' for i in range(num_features)]
    df = pd.DataFrame(data, columns=columns)
    
    return df

# 예시 사용법
num_samples = 100  # 샘플 수
num_features = 5   # 속성 수
min_val = 0        # 최소값
max_val = 10       # 최대값

synthetic_data = generate_synthetic_data(num_samples, num_features, min_val, max_val)

# CSV 파일 불러오기
blood_oxygen = pd.read_csv('/mnt/data/blood oxygen.csv')
heart_rate = pd.read_csv('/mnt/data/heart rate.csv')

# 데이터 병합
merged_data = pd.merge(blood_oxygen, heart_rate, on='User_ID')

# 새로운 합성 특성 생성
def create_synthetic_features(data):
    data['Oxygen_Heart_Ratio'] = data['Blood_Oxygen_Level'] / data['Heart_Rate']
    data['Synthetic_Feature'] = data['Blood_Oxygen_Level'] * 0.8 + data['Heart_Rate'] * 0.2
    return data

synthetic_merged_data = create_synthetic_features(merged_data)

# 합성 데이터 출력 및 저장
print(synthetic_merged_data.head())
synthetic_merged_data.to_csv('/mnt/data/synthetic_merged_data.csv', index=False)
