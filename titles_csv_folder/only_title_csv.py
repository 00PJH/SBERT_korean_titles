import pandas as pd

# 파일 경로
file_path = 'NewsResult_20240812-20240812.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 제목 열만 추출
df_titles_only = df[['제목']]

# 새로운 CSV 파일로 저장
output_path = 'NewsResult_20240812-20240812_only_titles.csv'
df_titles_only.to_csv(output_path, index=False, encoding='utf-8-sig')

output_path
