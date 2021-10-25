peline {
    agent { label 'master' }
	//options { skipDefaultCheckout false  }
    parameters {
        string(name: 'PHASE', defaultValue: 'BUILD', description: 'The stage to run this pipeline')
            }
    
   
      stages{
          stage("GitCheckout"){
		  when {
                expression { params.PHASE == 'BUILD' || params.PHASE == 'BUILD-ONLY' }
		  } 
            steps{   
              
               checkout([$class: 'GitSCM', branches: [[name: '*/master']], 
               extensions: [], 
               userRemoteConfigs: [[url: 'https://github.com/jenkins-docs/simple-python-pyinstaller-app.git']]])
              
		 }
     }
 
            stage("build"){
			when {
                expression { params.PHASE == 'BUILD' || params.PHASE == 'BUILD-ONLY' }
		  } 
               steps{
                 sh ''' 
                 ls -tlr
                 git init
                echo "build is done"
                  '''
                 }
            }
       stage("SonarScan"){
		when {
                expression { params.PHASE == 'BUILD' || params.PHASE == 'SONAR' }
		  } 
		
        steps {
        
        withSonarQubeEnv('Sonarqube') {
            dir (''){
                sh 'pwd && ls -ltr '
            sh ' sonar-scanner \
  -Dsonar.projectKey=chandra-python \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://127.0.0.1:9000 \
  -Dsonar.login=f91c93a33c107e2fffda0139fcd764c78b56c99d \
  -Dsonar.scm.disabled=true'
 	
            }
        }
                
       }
   }
        
     stage("NexusUpload"){
	 when {
                expression { params.PHASE == 'BUILD-NEXUS' || params.PHASE == 'NEXUS' }
		  } 
		  
            steps{
               
                sh 'pwd && ls -ltr '
                 //echo '********************NexusUpload********************'
                nexusArtifactUploader(
    nexusVersion: 'nexus3',
    protocol: 'https',
    nexusUrl: 'alm.repo-update.com/nexus',
    groupId: 'org.samples',
    repository: 'ADOP_Demo_Internal_Release',
    version: '$BUILD_NUMBER',
    credentialsId: 'Chandra-pipline-aditya',
    artifacts: [
        [artifactId: 'chandra-python-pipeline',
         classifier: '',
         file: 'chandra-python1' + '.tar.gz',
         type: 'gzip']
    ]
 )
   
            }
        }
     stage("Deploy"){
	when {
                expression { params.PHASE == 'BUILD' || params.PHASE == 'DEPLOY-ONLY' }
		  } 
	    //agent {   label "ec2-34-244-198-95.eu-west-1.compute.amazonaws.com" }
		          steps{
              echo "*************Deploy-Dev******************"
           sh '''
                 echo " Deployed using azure app services separertly."
          
	               '''
           
          }  
     }   
  }
}

