const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.createJob('push_notification_code_3', jobData);

    job
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (error) => {
        console.error(`Notification job ${job.id} failed: ${error}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });

    job.save((error) => {
      if (error) {
        console.error(`Notification job failed: ${error}`);
      } else {
        console.log(`Notification job created: ${job.id}`);
      }
    });
  });
};

export default createPushNotificationsJobs;
