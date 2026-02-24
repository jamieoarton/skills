# Get singular time entry

View a single time entry. \
 \
***Note:** A time entry that has a negative duration means that timer is currently running for that user.*

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/team/{team_id}/time_entries/{timer_id}": {
      "get": {
        "summary": "Get singular time entry",
        "tags": [
          "Time Tracking"
        ],
        "description": "View a single time entry. \\\n \\\n***Note:** A time entry that has a negative duration means that timer is currently running for that user.*",
        "operationId": "Getsingulartimeentry",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "timer_id",
            "in": "path",
            "description": "The ID of a time entry. \\\n \\\nThis can be found using the [Get Time Entries Within a Date Range](https://developer.clickup.com/reference/gettimeentrieswithinadaterange) endpoint.",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "1963465985517105840"
              ]
            }
          },
          {
            "name": "include_task_tags",
            "in": "query",
            "description": "Include task tags in the response for time entries associated with tasks.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_location_names",
            "in": "query",
            "description": "Include the names of the List, Folder, and Space along with `list_id`,`folder_id`, and `space_id`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_approval_history",
            "in": "query",
            "description": "Include the history of the approval for the time entry.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_approval_details",
            "in": "query",
            "description": "Include the details of the approval for the time entry.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "Content-Type",
            "in": "header",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "const": "application/json",
              "type": "string",
              "examples": [
                "application/json"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "Getsingulartimeentryresponse",
                  "required": [
                    "data"
                  ],
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "description": "",
                      "title": "Datum2",
                      "required": [
                        "id",
                        "wid",
                        "user",
                        "billable",
                        "start",
                        "end",
                        "duration",
                        "description",
                        "tags",
                        "source",
                        "at",
                        "task_location",
                        "task_tags",
                        "task_url"
                      ],
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "wid": {
                          "type": "string"
                        },
                        "user": {
                          "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1time_entries~1stop/post/responses/200/content/application~1json/schema/properties/data/properties/user"
                        },
                        "billable": {
                          "type": "boolean"
                        },
                        "start": {
                          "type": "string"
                        },
                        "end": {
                          "type": "string"
                        },
                        "duration": {
                          "type": "string"
                        },
                        "description": {
                          "type": "string"
                        },
                        "tags": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "source": {
                          "type": "string"
                        },
                        "at": {
                          "type": "string"
                        },
                        "approval_id": {
                          "type": "string",
                          "description": "ID of the associated approval"
                        },
                        "approval": {
                          "$ref": "#/paths/~1v2~1team~1%7Bteam_Id%7D~1time_entries/get/responses/200/content/application~1json/schema/examples/0/data/0/approval"
                        },
                        "task_location": {
                          "title": "TaskLocation",
                          "required": [
                            "list_id",
                            "folder_id",
                            "space_id",
                            "list_name",
                            "folder_name",
                            "space_name"
                          ],
                          "type": "object",
                          "properties": {
                            "list_id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "folder_id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "space_id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "list_name": {
                              "type": "string"
                            },
                            "folder_name": {
                              "type": "string"
                            },
                            "space_name": {
                              "type": "string"
                            }
                          },
                          "examples": [
                            {
                              "list_id": 1560300071,
                              "folder_id": 468300080,
                              "space_id": 22800253,
                              "list_name": "List",
                              "folder_name": "Folder",
                              "space_name": "Space"
                            }
                          ]
                        },
                        "task_tags": {
                          "type": "array",
                          "items": {
                            "title": "TaskTag",
                            "required": [
                              "name",
                              "tag_fg",
                              "tag_bg",
                              "creator"
                            ],
                            "type": "object",
                            "properties": {
                              "name": {
                                "type": "string"
                              },
                              "tag_fg": {
                                "type": "string"
                              },
                              "tag_bg": {
                                "type": "string"
                              },
                              "creator": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              }
                            },
                            "examples": [
                              {
                                "name": "content-request",
                                "tag_fg": "#800000",
                                "tag_bg": "#2ecd6f",
                                "creator": 301828
                              }
                            ]
                          },
                          "description": ""
                        },
                        "task_url": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": "timer_id",
                          "wid": "workspace_id",
                          "user": {
                            "id": 1,
                            "username": "first_name last_name",
                            "email": "test@gmail.com",
                            "color": "#08c7e0",
                            "initials": "JK",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                          },
                          "billable": false,
                          "start": "1592841559129",
                          "end": "1592845899021",
                          "duration": "4339892",
                          "description": "",
                          "tags": [],
                          "source": "clickup",
                          "at": "1592845899021",
                          "approval_id": "2d539936-119a-4927-9770-179f0a72e2e5",
                          "approval": {
                            "$ref": "#/paths/~1v2~1team~1%7Bteam_Id%7D~1time_entries/get/responses/200/content/application~1json/schema/examples/0/data/0/approval"
                          },
                          "task_location": {
                            "list_id": 1560300071,
                            "folder_id": 468300080,
                            "space_id": 22800253,
                            "list_name": "List",
                            "folder_name": "Folder",
                            "space_name": "Space"
                          },
                          "task_tags": [
                            {
                              "name": "content-request",
                              "tag_fg": "#800000",
                              "tag_bg": "#2ecd6f",
                              "creator": 301828
                            },
                            {
                              "name": "marketing-okr",
                              "tag_fg": "#800000",
                              "tag_bg": "#7C4DFF",
                              "creator": 301828
                            }
                          ],
                          "task_url": "https://staging.clickup.com/t/rnmuwz7"
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "data": [
                        {
                          "id": "timer_id",
                          "wid": "workspace_id",
                          "user": {
                            "id": 1,
                            "username": "first_name last_name",
                            "email": "test@gmail.com",
                            "color": "#08c7e0",
                            "initials": "JK",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                          },
                          "billable": false,
                          "start": "1592841559129",
                          "end": "1592845899021",
                          "duration": "4339892",
                          "description": "",
                          "tags": [],
                          "source": "clickup",
                          "at": "1592845899021",
                          "approval_id": "2d539936-119a-4927-9770-179f0a72e2e5",
                          "approval": {
                            "$ref": "#/paths/~1v2~1team~1%7Bteam_Id%7D~1time_entries/get/responses/200/content/application~1json/schema/examples/0/data/0/approval"
                          },
                          "task_location": {
                            "list_id": 1560300071,
                            "folder_id": 468300080,
                            "space_id": 22800253,
                            "list_name": "List",
                            "folder_name": "Folder",
                            "space_name": "Space"
                          },
                          "task_tags": [
                            {
                              "name": "content-request",
                              "tag_fg": "#800000",
                              "tag_bg": "#2ecd6f",
                              "creator": 301828
                            },
                            {
                              "name": "marketing-okr",
                              "tag_fg": "#800000",
                              "tag_bg": "#7C4DFF",
                              "creator": 301828
                            }
                          ],
                          "task_url": "https://staging.clickup.com/t/rnmuwz7"
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "data": [
                    {
                      "id": "timer_id",
                      "wid": "workspace_id",
                      "user": {
                        "id": 1,
                        "username": "first_name last_name",
                        "email": "test@gmail.com",
                        "color": "#08c7e0",
                        "initials": "JK",
                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                      },
                      "billable": false,
                      "start": "1592841559129",
                      "end": "1592845899021",
                      "duration": "4339892",
                      "description": "",
                      "source": "clickup",
                      "at": "1592845899021",
                      "task_location": {
                        "list_id": 1560300071,
                        "folder_id": 468300080,
                        "space_id": 22800253,
                        "list_name": "List",
                        "folder_name": "Folder",
                        "space_name": "Space"
                      },
                      "task_tags": [
                        {
                          "name": "content-request",
                          "tag_fg": "#800000",
                          "tag_bg": "#2ecd6f",
                          "creator": 301828
                        },
                        {
                          "name": "marketing-okr",
                          "tag_fg": "#800000",
                          "tag_bg": "#7C4DFF",
                          "creator": 301828
                        }
                      ],
                      "task_url": "https://staging.clickup.com/t/rnmuwz7"
                    }
                  ]
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Time Tracking"
    }
  ]
}
```