# -*- coding: utf-8 -*-
# __file__  : test_01.py
# __time__  : 2020/6/24 5:07 下午


# -*- coding: utf-8 -*-
# __author__: kevin
# __file__  : gitlab-sync.py
# __time__  : 2020/6/21 21:27

import gitlab
import os
from datetime import datetime, timedelta
import os

shfilename = "/Users/kevin/code/wemart/wmgit/git-pull-push.sh"

gl = gitlab.Gitlab("http://wmgit.wemart.cn", private_token="TnVJU68Zkxjsk52ScTCG")
page = 1
with open(shfilename, "w") as shf:
    shf.writelines(
        """function git_pull_push_remotes() {
    local_branches=`git branch|sed 's/\*//'`
    remote_branches=$*
    for br in $remote_branches; do
        if [[ $local_branches =~ $br ]]
        then
            git checkout $br && git pull && git push github $br
        else
            git checkout origin/$br -b $br && git push github $br
        fi
    done
}
    """
    )
    shf.write("\n")
    for page in range(1, 10):
        projects = gl.projects.list(
            sort="desc", order_by="last_activity_at", page=page, per_page=20
        )
        for project in projects:
            branches = project.branches.list()
            recent_branches = []
            for branch in branches:
                committed_date = datetime.strptime(
                    branch.commit["committed_date"][0:19], "%Y-%m-%dT%H:%M:%S"
                )
                if datetime.now() - committed_date < timedelta(days=3):
                    recent_branches.append(branch.name)
            if len(recent_branches) > 0:
                branch_names = ""
                for recent_branch in recent_branches:
                    branch_names += recent_branch + " "
                shf.writelines(
                    "cd /Users/kevin/code/wemart/wmgit/{} && git_pull_push_remotes {}".format(
                        project.path_with_namespace, branch_names
                    )
                )
                shf.write("\n")
os.system(shfilename)
