pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/ken3563/Localk', branch: 'dev')
      }
    }

    stage('List') {
      parallel {
        stage('List') {
          steps {
            sh 'ls -la'
          }
        }

        stage('Print file') {
          steps {
            sh 'cat /finalAPP/requirements.txt'
          }
        }

      }
    }

  }
}