pipeline {
    agent { label 'windows-chrome' }

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
                powershell '''
                    $ErrorActionPreference = 'Stop'
                    if (-not (Test-Path '.venv/Scripts/python.exe')) {
                        python -m venv .venv
                        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
                    }
                    & .venv/Scripts/python.exe -m pip install --upgrade pip
                    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
                    & .venv/Scripts/python.exe -m pip install -r requirements.txt
                    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
                '''
            }
        }

        stage('Run Selenium sign-in page check') {
            steps {
                powershell '''
                    $ErrorActionPreference = 'Stop'
                    New-Item -ItemType Directory -Force -Path selenium/robot/results | Out-Null
                    & .venv/Scripts/python.exe -m robot --variable HEADLESS:True --outputdir selenium/robot/results selenium/robot/teams_login.robot
                    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'selenium/robot/results/**', allowEmptyArchive: true
        }
    }
}
