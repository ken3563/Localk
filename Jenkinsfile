pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git 'https://github.com/ken3563/Localk/tree/main/finalAPP'
        git(url: 'https://github.com/ken3563/Localk/tree/main/finalAPP', branch: 'dev')
        git(url: 'https://github.com/ken3563/Localk/tree/dev/finalAPP', branch: 'dev')
      }
    }

  }
}