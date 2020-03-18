pipeline {
    agent any
    stages {
        stage('Environment'){
            steps {
                bat 'virtualenv loan_app'
                bat 'loan_app\\scripts\\activate'
                bat ' git branch: 'development', url: 'https://github.com/Prasad459/loan_app.git''
            }
        }
        stage('setupDB') {
            steps {
               bat 'python setupDB.py'
            }
        }
        stage('Build') {
            steps {
				// run the application server in the background
                bat 'START /B python loan_app.py'
            }
        }
        stage('SmokeTest') {
            steps {
                // smoke test the new application
                bat 'git branch -r'
                bat 'git checkout release'
                bat 'git pull'
                bat 'git merge development' 
                bat 'python smoketest.py'
                bat 'python seleniumtest.py
                //bat 'loan_app\\scripts\\deactivate'
            }
        }
        stage('merge into master branch'){
            steps{
                bat 'git branch -r'
                bat 'git checkout master'
                bat 'git pull'
                bat 'git merge release'
            }
        }
    }
    post {
        cleanup {
            bat 'del /f /q *.*'
           // deleteDir()
           echo 'Process completed'
        }
    }
    //Email notification about the build status//
    post {
        failure {
            mail to: 'team@example.com',
             subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
             body: "Something is wrong with ${env.BUILD_URL}"
    }
}
}
