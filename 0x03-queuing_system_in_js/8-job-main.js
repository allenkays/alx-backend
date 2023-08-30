import kue from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData);
    
    job.save((error) => {
      if (error) {
        console.error(`Notification job ${job.id} failed: ${error}`);
      } else {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (error) => {
      console.error(`Notification job ${job.id} failed: ${error}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
};

// Example usage
const queue = kue.createQueue();
const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  // Add more job objects here...
];

createPushNotificationsJobs(list, queue);
