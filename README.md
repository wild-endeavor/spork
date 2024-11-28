# Test repo

This is a test repo to figure out how git works.

Repo was forked at commit 7c99179e19282115348f5b0b805f303cde6f2262.

After that both made one non-conflicting PR to master.
https://github.com/unionai/spork/pull/2 -> ca5bdb2b6cbe2f66aafaea3fe02f1aaa578def3f
https://github.com/wild-endeavor/spork/pull/3 -> e10a966fd56dcfa802a38a691f34525805e90e8b

Finding the merge base results in the fork commit as expected.
```bash
$ git merge-base master upstream/master
7c99179e19282115348f5b0b805f303cde6f2262
```



ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork (master) $ git merge-base master upstream/master
7c99179e19282115348f5b0b805f303cde6f2262
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork (master) $ git fetch upstream
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork (master) $ git co -b try-sync
Switched to a new branch 'try-sync'
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork (try-sync) $ git merge upstream/master
Merge made by the 'ort' strategy.
 README.md | 8 +++++++-
 1 file changed, 7 insertions(+), 1 deletion(-)
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork (try-sync) $ git hs -n 3
*   865149c 2024-11-28T11:02:03-08:00 | (HEAD -> try-sync) Merge remote-tracking branch 'upstream/master' into try-sync (8 seconds ago) <Yee Hing Tong>
|\
| * e10a966 2024-11-28T10:35:47-08:00 | (upstream/master) Readme (#3) (26 minutes ago) <Yee Hing Tong>
* | ca5bdb2 2024-11-28T10:40:48-08:00 | (origin/master, origin/HEAD, master) add a class and move a function (#2) (21 minutes ago) <Yee Hing Tong>
|/
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork (try-sync) $ git co -b async/tasks-agent-local
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork (try-sync) $
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork (try-sync) $ git merge-base try-sync upstream/master
e10a966fd56dcfa802a38a691f34525805e90e8b
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork (try-sync) $ git co master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.

try rebasing
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork [flyte-sandbox] (master) $ git co -b try-sync-rebase
Switched to a new branch 'try-sync-rebase'
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork [flyte-sandbox] (try-sync-rebase) $ git rebase upstream/master
Successfully rebased and updated refs/heads/try-sync-rebase.
ytong@Yees-MacBook-Pro:~/go/src/github.com/unionai/spork [flyte-sandbox] (try-sync-rebase) $ git hs -n 5
* cc53fe7 2024-11-28T10:40:48-08:00 | (HEAD -> try-sync-rebase) add a class and move a function (#2) (5 seconds ago) <Yee Hing Tong>
* e10a966 2024-11-28T10:35:47-08:00 | (upstream/master) Readme (#3) (46 minutes ago) <Yee Hing Tong>
* 7c99179 2024-11-28T10:16:30-08:00 | add a second folder (65 minutes ago) <Yee Hing Tong>
* bf2d064 2024-11-28T10:04:08-08:00 | add some dumb code (78 minutes ago) <Yee Hing Tong>
* 4726dca 2024-11-28T09:55:30-08:00 | delete (86 minutes ago) <Yee Hing Tong>

Using merge strategy (`try-sync` branch) so as to better keep history.

$ git merge-base master upstream/master
e10a966fd56dcfa802a38a691f34525805e90e8b
