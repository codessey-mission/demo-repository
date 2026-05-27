# StudyLog

StudyLog는 GitHub 협업 과제를 수행하면서 함께 만드는 작은 Python CLI 프로그램입니다.
학습 항목을 추가하고, 완료 처리하고, 통계를 확인하고, Markdown 보고서로 내보낼 수 있습니다.

## 팀

- A: 황정현 (newcode99) - 모델/저장소
- B: 이현민 (seven2762) - CLI
- C:  권순형 (soonvro) - 통계/내보내기

## 실행 예시

기능 PR이 병합된 뒤 아래처럼 실행합니다.

```bash
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json add "GitHub Flow 학습" --minutes 40 --note "Issue와 PR 연결"
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json list
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json complete 1
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json stats
PYTHONPATH=src python3 -m studylog.cli --data ./studylog.json export-md ./studylog-report.md
```

## 개발 검증

변경 사항은 아래 기준을 만족해야 합니다.

- 기존 테스트가 모두 통과한다.
- 새 기능이나 동작 변경에는 관련 테스트를 추가한다.
- CLI 예시 명령이 정상적으로 실행되는지 확인한다.
- README와 사용 문서가 실제 동작과 다르지 않은지 확인한다.

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test*.py'
```

## 문서

- [협업 규칙](docs/CONTRIBUTING.md)
- [사용법](docs/usage.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [트러블슈팅 기록](docs/troubleshooting-log.md)
- [제출 인덱스](SUBMISSION.md)
