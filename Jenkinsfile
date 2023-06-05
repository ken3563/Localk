pipeline {
  agent any
  stages {
    stage('TP') {
      steps {
        git(url: 'https://github.com/ken3563/Localk/', branch: 'test_branch')
      }
    }

    stage('Log') {
      steps {
        sh 'ls -la'
      }
    }

  }
}