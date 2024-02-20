from dagster import (Definitions,
                     load_assets_from_modules,
                     AssetSelection,
                     ScheduleDefinition,
                     define_asset_job)

from .assets import resources

# Define a job that will materialize the assets
big_star_job = define_asset_job("big_star_job", selection=AssetSelection.all())

# A ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
big_star_schedule = ScheduleDefinition(
    job=big_star_job,
    cron_schedule="0 * * * *",  # every hour
)

defs = Definitions(assets=load_assets_from_modules([assets]),
                   resources=resources,
                   schedules = [big_star_schedule],
    )
