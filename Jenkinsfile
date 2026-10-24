pipeline {
    agent { label 'linux-chrome' }

    options {
        timestamps()
        timeout(time: 15, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Selenium dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r selenium/microsoftteams/requirements.txt
                '''
            }
        }

        stage('Run Selenium sign-in page check') {
            steps {
                sh '''
                    mkdir -p selenium/microsoftteams/robot/results
                    xvfb-run -a .venv/bin/python -m robot \\
                      --outputdir selenium/microsoftteams/robot/results \\
                      selenium/microsoftteams/robot/teams_login.robot
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'selenium/microsoftteams/robot/results/**', allowEmptyArchive: true
        }
    }
}
