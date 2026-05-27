# StudyLog Usage

이 문서는 StudyLog CLI 사용법을 기록한다.

## 기본 명령

기능 PR이 병합되면 아래 명령들이 제공된다.

- `add`: 학습 항목 추가
- `list`: 학습 항목 목록 조회
- `complete`: 학습 항목 완료 처리
- `delete`: 학습 항목 삭제
- `stats`: 학습 통계 조회
- `export-md`: Markdown 보고서 내보내기

## add / list 예시

```bash
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json add "GitHub Flow 학습" --minutes 40 --note "Issue와 PR 연결"
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json list
```

## complete / delete 예시

```bash
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json complete 1
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json delete 1
```

## stats 예시

```bash
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json stats
```

## stats 예시

```bash
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json stats
```

## export-md 예시

```bash
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json export-md ./studylog-report.md
```
