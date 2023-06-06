pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/ken3563/Localk', branch: 'dev')
      }
    }

    stage('List') {
      steps {
        sh 'ls -la'
      }
    }

  }
}