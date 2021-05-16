#!/usr/bin/env python3
import io
from aws_cdk import core

from mwaa_redshift.mwaa_redshift_stack import MwaaRedshiftStack
from mwaa_redshift.mwaa_redshift_vpc import MwaaRedshiftVPC

# this assumes you have setup a MWAA environment and you need to provide
# - the DAGS folder "mwaadag"
# - the security group created and used by MWAA "mwaa-sg"
# - the vpc id for your mwaa environment

env_EU=core.Environment(region="eu-west-1", account="XXXXXXXXXX")
props = {
    'redshifts3location': '{your new s3 bucket for redhshift}',
    'mwaadag' : '{your airflow dag s3 bucket}',
    'mwaa-sg':'{your mwaa sg group}',
    'mwaa-vpc-id':'{your mwaa vpc id}',
    'redshiftclustername':'mwaa-redshift-clusterxxx'
    }

app = core.App()

redshift_vpc = MwaaRedshiftVPC(
    scope=app,
    id="MWAA-Redshift-VPC",
    env=env_EU,
    props=props
)

redshift_env = MwaaRedshiftStack(
    scope=app,
    id="MWAA-Redshift-Cluster",
    vpc=redshift_vpc.vpc,
    env=env_EU,
    props=props
)


app.synth()
