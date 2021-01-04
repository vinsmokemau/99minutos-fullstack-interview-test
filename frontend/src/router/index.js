import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListBranches from '@/components/branches/ListBranches'
import BranchDetail from '@/components/branches/BranchDetail'
import CommitDetail from '@/components/branches/CommitDetail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/branches/',
      name: 'ListBranches',
      component: ListBranches
    },
    {
      path: '/branches/:branchName/',
      name: 'BranchDetail',
      component: BranchDetail
    },
    {
      path: '/commits/:commitId/',
      name: 'CommitDetail',
      component: CommitDetail
    },
  ],
  mode: 'history',
})
