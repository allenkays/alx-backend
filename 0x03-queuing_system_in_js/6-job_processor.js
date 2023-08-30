import kue from 'kue';

const queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

/* Gracefully handle process exit */
process.on('SIGINT', () => {
  queue.shutdown(5000, () => {
    process.exit(0);
  });
});
