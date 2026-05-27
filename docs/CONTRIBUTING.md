# Contributing Guide

## 브랜치 전략: GitHub Flow

- `main`은 항상 실행 가능하고 테스트가 통과하는 상태로 유지한다.
- 모든 작업은 `feature/*`, `docs/*`, `fix/*`, `chore/*` 브랜치에서 진행한다.
- 작업이 끝나면 Pull Request를 열고, 최소 1명 이상의 리뷰 승인을 받은 뒤 병합한다.

우리 팀이 GitHub Flow를 선택한 이유:
1. 작은 CLI 프로그램을 빠르게 나눠 개발하기에 단순하고 이해하기 쉽다.
2. 모든 변경이 PR과 리뷰를 거치므로 main이 깨질 가능성을 줄일 수 있다.
3. Issue, PR, 리뷰 기록이 남아 과제 증빙과 실무 협업 연습을 동시에 만족한다.

## 브랜치 네이밍 규칙

- 기능: `feature/<member-slug>-<topic>`
- 문서: `docs/<member-slug>-<topic>`
- 수정: `fix/<member-slug>-<topic>`
- 실습/기타: `practice/<member-slug>-<topic>`

예시:

- `feature/a-core-model`
- `feature/b-cli-add-list`
- `feature/c-stats`
- `practice/a-amend`

## 커밋 메시지 컨벤션

권장 형식:

- `feat: add study entry model`
- `fix: validate negative study minutes`
- `docs: record conflict resolution case`
- `test: add cli complete command tests`
- `chore: bootstrap project structure`

금지 예시:

- `update`
- `fix`
- `temp`
- `wip`
- `final`
- `edit file`

커밋 메시지에는 무엇을 바꿨는지 드러나야 한다.

## Issue / PR 규칙

모든 작업은 Issue를 먼저 만들고 PR과 연결한다.

PR 본문 필수 항목:

- 연결 이슈: `Closes #<issue_number>`
- 변경 사항(What)
- 변경 이유(Why)
- 테스트/검증 방법(How)

## 코드 리뷰 규칙

- 본인 PR은 본인이 승인하지 않는다.
- “LGTM”, “좋아요”만 단독으로 남기지 않는다.
- 파일/함수/동작/테스트를 근거로 질문, 리스크, 개선안을 남긴다.
- 작성자는 최소 1회 이상 리뷰에 답하거나 수정 커밋으로 반영한다.

좋은 리뷰 예시:

> `src/studylog/storage.py`의 `complete()`가 없는 id를 받을 때 조용히 실패합니다. CLI 사용자가 원인을 알 수 있도록 `False`를 반환하고 CLI에서 메시지를 출력하면 좋겠습니다.

## 충돌 대응 흐름

1. 충돌이 발생한 브랜치와 파일을 팀 채널에 공유한다.
2. 작성자와 관련 작업자가 어떤 변경을 살릴지 합의한다.
3. 로컬에서 `git merge origin/main` 또는 필요한 절차로 충돌을 재현한다.
4. 충돌 마커를 확인하고 최종 코드를 만든다.
5. `docs/conflict-resolution.md`에 상황, 마커, 해결 과정, 결과를 기록한다.
6. 테스트를 실행하고 PR 브랜치에 push한다.

## 테스트 규칙

기능 PR은 가능한 한 테스트를 포함한다.

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test*.py'
```
