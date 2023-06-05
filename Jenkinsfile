pipeline {
  agent any
  stages {
    stage('TP') {
      steps {
        git(url: 'https://github.com/ken3563/Localk/', branch: 'test_branch')
        git(branch: 'test_branch', url: 'https://github.com/ken3563/Localk/tree/test_branch/finalAPP')
      }
    }

    stage('Log') {
      steps {
        sh 'ls -la'
      }
    }

  }
}