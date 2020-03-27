   pipeline {
    agent any
    stages {
        stage('Environment'){
            steps {
                deleteDir()
                bat 'virtualenv loan_app'
                bat 'loan_app\\scripts\\activate'
                //this code will clone the specific repository//
               checkout([$class: 'GitSCM', branches: [[name: 'development']],
                 doGenerateSubmoduleConfigurations: false, extensions: [], 
                 submoduleCfg: [], userRemoteConfigs: 
                 [[url: 'https://github.com/Prasad459/loan_app.git']]])
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
        stage('slack notification for build status'){
            steps{
             slackSend baseUrl: 'https://hooks.slack.com/services/', channel: 'jenkins-pipeline', color: ' good', message: 'The Build stage is successful', notifyCommitters: true, teamDomain: 'Workoopolis', tokenCredentialId: '495c3cb7-0376-4873-8608-7fb4a027690a'
            }
            
        }
         stage('selenium') {
            steps {
                // smoke test the new application 
                bat 'python smoketest.py'
                //bat 'loan_app\\scripts\\deactivate'
            }
        }
        stage('slack notification for smoketest'){
            steps{
             slackSend baseUrl: 'https://hooks.slack.com/services/', channel: 'jenkins-pipeline', color: ' good', message: 'The smoke test is successful', notifyCommitters: true, teamDomain: 'Workoopolis', tokenCredentialId: '495c3cb7-0376-4873-8608-7fb4a027690a'
            }
            
        }
         
        stage('merge into release branch') {
            steps {
                bat 'git branch -r'
                bat 'git checkout  release'
                 bat 'git branch'
                  //bat 'git clean -d -f'
                  bat 'git fetch origin'
                  bat 'git pull origin release'
                 bat 'git merge origin/development'
               
              
                
            }
        }
        stage('merge into master branch') {
            steps {
                bat 'git branch -r'
                bat 'git add .'
               bat 'git commit -m "merge into master branch"'
                bat 'git checkout  master'
                //bat 'git clean -d -f'
                bat 'git branch'
                 
                  bat 'git fetch origin'
                  bat 'git pull origin master'
                  bat 'git.exe merge --strategy=ours release'
                 //bat 'git merge origin/release'
            }
        }
        stage('Job status'){
            steps{
             slackSend baseUrl: 'https://hooks.slack.com/services/', channel: 'jenkins-pipeline', color: ' good', message: 'The Job is successful', notifyCommitters: true, teamDomain: 'Workoopolis', tokenCredentialId: '495c3cb7-0376-4873-8608-7fb4a027690a'
           
                
            }
            
            
        }
    
        
    }
}
