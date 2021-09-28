node('docker') {
    def workspace = pwd()
    stage('Git checkout') {
        checkout scm
    }
    stage('Build image') {
        sh "docker-compose -f ${workspace}/docker-compose.yml up --build --force-recreate"
    }
    stage('Upload RPMS to Katello') {
      withCredentials([
        string(credentialsId: 'katello-host', variable: 'KATELLO_HOST'),
        usernamePassword(credentialsId: 'katello-user', usernameVariable: 'KATELLO_USER', passwordVariable: 'KATELLO_PASSWORD')
      ]){
        sh "hammer -s ${KATELLO_HOST} -u ${KATELLO_USER} -p ${KATELLO_PASSWORD} repository upload-content --id 1767 --path RPMS/x86_64/*el6.x86_64.rpm"
        sh "hammer -s ${KATELLO_HOST} -u ${KATELLO_USER} -p ${KATELLO_PASSWORD} repository upload-content --id 1760 --path RPMS/x86_64/*el7.x86_64.rpm"
      }
    }
    stage('Remove unused Docker image') {
        sh "docker-compose -f ${workspace}/docker-compose.yml rm -fs"
    }
}