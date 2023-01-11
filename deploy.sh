fission spec init
fission env create --spec --name onb-br-enum-doc-tp-env --image nexus.sigame.com.br/fission-onboarding-br-enum-document-type:0.2.0-0 --poolsize 0 --version 3 --imagepullsecret "nexus-v3" --spec
fission fn create --spec --name onb-br-enum-doc-tp-fn --env onb-br-enum-doc-tp-env --code fission.py --targetcpu 80 --executortype newdeploy --maxscale 3 --requestsperpod 10000 --spec
fission route create --spec --name onb-br-enum-doc-tp-rt --method GET --url /enum/document_type --function onb-br-enum-doc-tp-fn
