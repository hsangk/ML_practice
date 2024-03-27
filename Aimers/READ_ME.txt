영업 성공 여부 분류
1. 영업 성공 여부 분류 경진대회 개요
최근 기계학습 분야가 크게 발전하게 된 만큼 연구도 활발해져서 기존의 전통적인 모델보다 더 높은 성능을 내는 모델도 다수 등장하고 있습니다. 더불어서 영업 과정에서 전환 가능성이 높은 고객에게 영업 자원을 집중하기 위해 고객의 전환 여부를 예측하기 위해 기계학습을 도입하고 있습니다.

따라서 이번 경진대회에서는 고객의 다양한 정보를 보고 해당 고객이 전환 고객인지 아닌지를 판단하는 모델을 구현하고 그 성능을 비교하고자 합니다.

2. 데이터셋 구성
2.1 모델 학습용 데이터셋
이번 경진대회에서 사용할 데이터 셋을 살펴보도록 하겠습니다.

데이터 셋은 고객의 다양한 정보를 기록한 데이터와 해당 고객의 영업이 성공으로 전환되었는지 알려주는 라벨 데이터로 이루어져 있습니다.

고객 정보를 기록한 데이터는 아래와 같습니다.

Field	설명
bant_submit	MQL 구성 요소들 중 [1]Budget(예산), [2]Title(고객의 직책/직급), [3]Needs(요구사항), [4]Timeline(희망 납기일) 4가지 항목에 대해서 작성된 값의 비율
customer_country	고객의 국적
business_unit	MQL 요청 상품에 대응되는 사업부
com_reg_ver_win_rate	Vertical Level 1, business unit, region을 기준으로 oppty 비율을 계산
customer_idx	고객의 회사명
customer_type	고객 유형
enterprise	Global 기업인지, Small/Medium 규모의 기업인지
historical_existing_cnt	이전에 Converted(영업 전환) 되었던 횟수
id_strategic_ver	(도메인 지식) 특정 사업부(Business Unit), 특정 사업 영역(Vertical Level1)에 대해 가중치를 부여
it_strategic_ver	(도메인 지식) 특정 사업부(Business Unit), 특정 사업 영역(Vertical Level1)에 대해 가중치를 부여
idit_strategic_ver	Id_strategic_ver이나 it_strategic_ver 값 중 하나라도 1의 값을 가지면 1 값으로 표현
customer_job	고객의 직업군
lead_desc_length	고객이 작성한 Lead Descriptoin 텍스트 총 길이
inquiry_type	고객의 문의 유형
product_category	요청 제품 카테고리
product_subcategory	요청 제품 하위 카테고리
product_modelname	요청 제품 모델명
customer_country.1	담당 자사 법인명 기반의 지역 정보(대륙)
customer_position	고객의 회사 직책
response_corporate	담당 자사 법인명
expected_timeline	고객의 요청한 처리 일정
ver_cus	특정 Vertical Level 1(사업영역) 이면서 Customer_type(고객 유형)이 소비자(End-user)인 경우에 대한 가중치
ver_pro	특정 Vertical Level 1(사업영역) 이면서 특정 Product Category(제품 유형)인 경우에 대한 가중치
ver_win_rate_x	전체 Lead 중에서 Vertical을 기준으로 Vertical 수 비율과 Vertical 별 Lead 수 대비 영업 전환 성공 비율 값을 곱한 값
ver_win_ratio_per_bu	특정 Vertical Level1의 Business Unit 별 샘플 수 대비 영업 전환된 샘플 수의 비율을 계산
business_area	고객의 사업 영역
business_subarea	고객의 세부 사업 영역
lead_owner	영업 담당자 이름
is_converted	영업 성공 여부. True일 시 성공.
다양한 feature가 있으며, 이 대회에서 예측해야 하는 값은 is_converted입니다.

2.2 제출용 테스트 데이터셋
학습용 데이터 셋으로 적절한 모델을 찾아 훈련까지 마쳤다면, 다음으로 제출을 위해 제출용 테스트 데이터 셋을 읽어들여 모델에 적용해야 합니다. 제출용 테스트 데이터는 학습 데이터와 마찬가지로 CSV 파일에 기록되어 있습니다. 파일의 이름은 submission.csv입니다.

다른 칼럼은 동일하지만, id는 학습 데이터에는 없는 칼럼이며, 테스트 데이터의 is_converted는 모두 비어있습니다.

id: 고객의 고유한 번호입니다. 고객의 순서가 섞인 경우에도 올바른 채점이 진행되기 위한 값으로, 채점 시 id와 is_converted를 비교하면서 평가합니다. 따라서 임의로 id칼럼을 제거하거나 변경하면 0점 처리될 수 있습니다.

제출용 데이터는 공정한 평가를 위해 일부 데이터를 추출한 것으로 학습용 데이터와 True와 False의 분포가 다릅니다.

 
4. 채점 방법
채점을 위해 submission.csv 파일을 읽고 저장해야 합니다. 읽은 파일을 2.2의 안내의 따라 값을 채워 넣은 후에 나온 테스트 데이터를 학습된 모델에 적용합니다. 모델에서 나온 예측 결과는 아래와 같은 형태의 CSV 파일로 저장하여야 합니다. 파일 이름은 submission.csv로 해야 합니다.

초기 디렉터리에 submission.csv파일을 저장하였다면, 오른쪽 위의 제출 버튼을 클릭해 결과를 확인할 수 있습니다.