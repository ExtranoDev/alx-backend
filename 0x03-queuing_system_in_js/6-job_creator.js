import { createQueue } from 'kue';

const push_notification_code = createQueue();

const data = {
  'phoneNumber': '+2130098674',
  'message': 'Welcome Big Head'
};

const job = push_notification_code.create('data', data).save(
  function (err) {
    if (!err) console.log(`Notification job created: ${job.id}`);
  }
);

job.on('complete', function(result) {
  console.log('Notification job completed');
});
job.on('failed', function(result) {
  console.log('Notification job failed');
});
