# 원화·이미지 에셋·프롬프팅

## 참조의 권위와 산출물 역할

같은 캐릭터의 머리·얼굴·체형·의상·장비·핵심 색을 기준 시트로 정한다. 상충하는 참조는 무엇을 따라야 하는지 지정한다. A는 정체성, B는 구도, C는 공간 재료, D는 모션 순서처럼 역할을 부여한다. 여러 입력을 넣는 것이 자동으로 일관성을 보장하지 않는다.

전투 원안은 작은 실루엣과 무기, 스탠딩은 얼굴과 대화 몸짓, 삽화는 사건과 구도, 선택 초상은 식별 가능한 얼굴 크롭, 기술 아이콘은 행동/무기/속성을 설명한다. 기존 도트를 확대해 스탠딩을 대신하거나 원안의 중립 포즈를 모든 삽화에 복사하지 않는다. 얼굴을 바꾸지 않으면서 장면에 맞는 자세를 만든다.

원근이 틀린 프랍, 다른 체형, 구조가 다른 의상은 확대/색상 수정만으로 해결하기 어렵다. 참조 교체 또는 재생성을 검토한다. 그림이 예쁘다는 평가와 같은 인물/같은 물건이라는 판정을 따로 한다. 가까이 보기 삽화와 맵 프랍도 같은 디자인인지 대조한다.

## 요청 작성

먼저 목적과 통과 조건을 정한다. 산출물 역할→정체성→행동/구도→공간/카메라→규격→보존 조건→금지→검수 기준 순으로 조립하되 요청에 필요한 항목만 쓴다. ‘상용 퀄리티’보다 측정 가능한 전신 여백·접점·프레임 정합이 유용하다.

```text
Create {output_role} for {specific_event_or_action}.
Reference A controls identity and costume; B controls composition only.
Preserve {identity_or_layout_invariants}.
Use {camera_perspective_material_and_frame_constraints}.
Keep {safe_margins_and_alpha_requirements}.
Do not add {unrelated_or_baked_elements}.
Output {actually_supported_dimensions_format_duration}.
```

이것은 미실행 템플릿이다. 도구가 지원하지 않는 길이/해상도를 프롬프트만으로 보장하지 않는다. 영상 생성 옵션과 프레임 추출 설정은 따로 기록한다. 실제 이미지 생성/편집을 수행할 때는 사용 가능한 해당 도구/스킬의 지침을 따른다. 이 문서가 특수 API나 우회 클라이언트를 만드는 이유가 되어서는 안 된다.

## 편집과 업스케일

디자인 개선과 보존형 업스케일을 구분한다. 좋은 모션의 해상도만 낮다면 전체 시트의 순서·셀·접점·위상·투명 여백을 보존하는 편집을 우선 비교한다. 독립 프레임 재생성은 시간적 형태 드리프트를 만들 수 있다. ‘보존’ 요청이 실제 보존의 증거는 아니므로 입력/출력 접촉 시트와 재생을 비교한다.

```text
Edit this atlas while preserving frame count/order, cell layout,
contact anchors and transparent margins. Enhance {material} consistently.
Do not move contact points, invent frames or crop the silhouette.
```

한 번에 바꾸는 결함 축을 줄이면 진단하기 쉽다. 근본 구조가 틀린 결과를 국소 편집으로 끝없이 살리려 하지 않는다. 승인된 기존 자산·공개 자산·코드 합성·생성형 편집·신규 생성의 적합성과 비용을 비교한다. 도구 선호와 유료 생성 보류는 프로젝트별 지시를 따른다.

## 기록과 반입

작업 ID / 입력 경로·역할 / 실제 요청 본문 / 도구와 옵션 / 출력·마스터 경로 / 권리·출처 / 선택·탈락 이유 / 게임 크기의 검수 / 런타임 연결을 기록한다. 요청 정의, 생성 완료, 반입 완료, 시각 승인 상태를 구분한다. 마스터를 배포 최적화 때문에 삭제하지 않는다. 생성형 편집으로 원본의 라이선스 의무가 사라지지 않는다.

스타일이 맞는 정지 그림만으로 모션 승인을 하지 않는다. 모션은 [전용 지침](sprites-motion.md), 공개 자산 확보는 [리서치](research-handoff.md), 맵 물건은 [공간 지침](world-cinematics.md)을 읽는다.
